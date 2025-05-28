// ...existing code...
document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById("loginForm");
    const usernameInput = document.getElementById("username");
    const passwordInput = document.getElementById("password");

    loginForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent the default form submission

        const username = usernameInput.value.trim();
        const password = passwordInput.value.trim();

        if (validateForm(username, password)) {
            // 發送 AJAX 請求到 Flask 後端
            fetch('http://localhost:3000/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            })
            .then(async response => {
                const data = await response.json();
                if (response.ok) {
                    alert(data.message);
                    window.location.href = '../../homeScreen.html'; // 登入成功導向主畫面
                } else {
                    alert(data.message);
                }
            })
            .catch(error => {
                alert('伺服器錯誤，請稍後再試');
                console.error(error);
            });
        } else {
            alert("Please enter a valid username and password.");
        }
    });

    function validateForm(username, password) {
        return username !== "" && password !== "";
    }
});
// ...existing code...