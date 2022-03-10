// install was a pain, but i did it via conda. had to also create /data/db and change permissions via chown robbydivine /data/db
// install help from: https://www.youtube.com/watch?v=DX15WbKidXY (brew was rec'd but took forever)
// conda activate mongodb
// in one tab: mongod
// in other, launching a js shell: mongo

show dbs
use newDb // creates new db if not made, otherwise switch to db

show collections // collections are like indiv tables within each db

// insert document into new or existing collection. can have multiple collections per db
db.collection1.insert([
    { h1: "val1", id: 1 },
    { h1: "val2", id: 2, newH: true },
    { h1: "val3", id: 3, newH: true },
    {
        h1: "val4", id: 4, newObj: {
            key1: 1,
            key2: 2
        }
    }
])
db.collection1.find() // search for all vals
db.collection1.find({ id: 2 }) // returns only newH

// updating. first find with first arg obj, then update using .updateOne() or .updateMany() and $set operator
db.collection1.updateOne({ id: 3 }, { $set: { newH: false } }) // updates newH

// delete using .deleteOne() or .deleteMany()
db.collection1.deleteOne({ id: 2 })
db.collection1.deleteMany({}) // deletes all

// access nested properties
db.collection1.find({ 'newObj.key1': 1 })

// other operators @ https://docs.mongodb.com/manual/reference/operator/query/
db.collection1.find({ id: { $gt: 1 } }) // returns entries where id > 1
db.collection1.find({ id: { $in: [2, 3] } }) // entries where id is in the array [2,3]
// can also do $and $or $ne (not equal), etc