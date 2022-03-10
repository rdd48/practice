// so js is single-threaded, but browser under hood can execute code asynchronously
// therefore js can handoff tasks to the browsers web apis to run in background
// so we need to write functions that tell js what to do in case of success or failure
// since we can't wait for that success or failure
// enter: promises, aka an object representing eventual completion or failure of async js operation

const fakeRequest = input => {
    return new Promise((resolve, reject) => {
        // set criteria for resolve or reject, e.g. randomly
        const rand = Math.random();
        if (rand >= 0.5) {
            resolve(`Success! Rand is ${rand}`)
        } else {
            reject(`Failure! Rand is ${rand}`)
        }
    })

}

fakeRequest('input1')
    .then((data) => {
        console.log('it worked!');
        console.log(data) // will log the resolve message above ("Success! ...")
        // can layer more function calls here (or later)
        return fakeRequest('input2')
    })
    .then(() => {
        console.log('it worked again!');

    })
    .catch((err) => {
        console.log('it failed!');
        console.log(err) // logs the reject message
    })

// async functions: return a promise
const myAsync = async () => {
    return 'This returns a resolved promise!'
}

const myAsyncReject = async () => {
    throw new Error('returns a rejecte promise!')
    // throw "error!" works too
}

// another example, remember this returns a promise
const login = async (username, password) => {
    if (!username || !password) { throw 'Missing Credentials' }
    else if (password === 'correctPw') { return 'Welcome!' }
    else { throw 'Invalid Password!' }
}

async function myFunction() {
    let myPromise = new Promise((resolve) => {
        resolve('test')
    })
    await myPromise;
}

// await keyword: pauses execution of function until proise is resolved
async function myFunc() {
    await setTimeout(console.log('wait 1 s', 1000));
    await setTimeout(console.log('wait 1 s', 1000));
    await setTimeout(console.log('wait 1 s', 1000));

    try {
        let data = fakeRequest(1)
        console.log(data)
    } catch (err) {
        console.log(err)
    }
    return 'Done!'
}

login('un', 'pw')
    .then(msg => console.log(msg))
    .catch(err => console.log(err))

// reminder: delay function
setTimeout(myFunc, delayTimeInMs)

