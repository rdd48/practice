// ajax: asynchronous js and xml
// ajax used to make requests. result of request is typically JSON (as a str)

// parse json into obj
const jsonStr = '{"1": 1, "2": 2}'
const parsedData = JSON.parse(jsonStr)
const unparseData = JSON.stringify(parsedData)

// Postman is a GUI used to make requests to APIs
// useful for debugging

// fetch api
fetch('myapitest.com')
    .then(res => {
        console.log('response', res)
        return res.json() // returns a promise
    })
    .then(data => {
        console.log(data) // this is the request
    })
    .catch(err =>
        console.log('oh no!', err))

// use axios to make even more simple fetch Promises
// need to add html script: <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
axios.get('mygetrequest.com')
    .then(res => console.log(res.data.ticker.price))
    .catch(err => console.log(err))

const fetchBitcoinPrice = async () => {
    try {
        const res = await axios.get('bitcoinapi.com');
        console.log(res.data.ticker.price);
    }
    catch (e) {
        console.log(e);
    }
}

// axios headers
const getDadJoke = async () => {
    // headers object from this api's docs
    const config = { headers: { Accept: 'application/json' } };
    const res = await axios.get('https://icanhazadjoke.com', config);
    console.log(res.data.joke)
}

// XMLHttpRequest: old way, works with IE, but harder/dumb
const req = new XMLHttpRequest();
req.onload = () => {
    const data = JSON.parse(this.responseText);
}
req.onerror = () => console.log('error');
req.get('GET', 'myurl.com');
req.send();