const form = document.querySelector('#searchForm')

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    removeImage();

    const input = document.querySelector('input');

    // could also do: form.elements.query.value
    const searchTerm = input.value

    // cound also do: await axios.get(`http://api.tvmaze.com/search/shows?q=${searchTerm}`)
    const config = { params: { q: searchTerm } }
    const res = await axios.get('http://api.tvmaze.com/search/shows', config)

    for (let s of res.data) {
        makeImage(s);
    }

})

const removeImage = () => {
    const allImg = document.querySelectorAll('IMG');
    for (let img of allImg) {
        img.remove();
    }
}

const makeImage = s => {

    if (s.show.image) {
        const imgSrc = s.show.image.medium;
        const img = document.createElement('IMG');
        img.src = imgSrc;
        document.body.append(img);
    }
}