
// run via node filename.js
for (let i = 0; i < 3; i++) {
    console.log('hello from node script')
}

// imports
const fs = require('fs');
// imports of local scripts requires scripts to module.exports an object
const { add, PI } = require('./node_exports.js')
console.log(PI)

// process object is node-specific and provides useful info like sys or os
// process.argv like python argv. get arguments after first 2 objects
// so e.g. running $ node node.js arg1, process.argv[2] is 'arg1'

// fs module like os, lets us manage files/dirs
// Sync-suffixed commands are synchronous versions
// fs.mkdirSync('new_dir');

// start node REPL (like ipython) by typing node in terminal
// .help to get some commands
// no dom (i.e. window or document.)