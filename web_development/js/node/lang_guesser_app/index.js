// using packages franc & langs
// cl: npm init; npm i franc; npm i langs

// const franc = require('franc');
import { franc } from "franc";
import langs from "langs";
import colors from "colors";

const inputText = franc(process.argv[2]);

const language = langs.where('3', inputText); // converts 3 letter code to language
// const language = langs.where('3', 'eng'); // converts 3 letter code to language

if (langs.code === 'und') {
    console.log('could not find');
} else {
    console.log(`${language.name}`.green);
}


