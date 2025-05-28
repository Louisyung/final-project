const options = {
    method: 'GET', 
    headers: {
        Authorization: 'Bearer <app-NLaNtrOQfNroM1lYHC78mQij>'
    }
    };

fetch('https://api.dify.ai/v1/messages?limit=20', options)
  .then(response => response.json())    //轉換為json格式
  .then(response => console.log(response))
  .catch(err => console.error(err));