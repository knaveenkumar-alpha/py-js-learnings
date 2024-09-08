/* 
File handling in JavaScript is commonly done on the server side using Node.js, as browser-based JavaScript does not have direct access
 to the file system due to security reasons. In Node.js, the fs (File System) module is used for file handling operations such as 
 reading, writing, updating, and deleting files.

Basic File Handling Operations in Node.js
1. Reading Files
2. Writing to Files
3. Appending to Files
4. Deleting Files
5. Renaming Files
*/

// Asynchronous Reading:
console.log("============================ Asynchronous Reading =======================================")
const fs = require('fs');

fs.readFile('example.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});

console.log("============================ Synchronous Reading =======================================")
const fs1 = require('fs');

try {
    const data = fs1.readFileSync('example.txt', 'utf8');
    console.log(data);
} catch (err) {
    console.error(err);
}

console.log("============================ Asynchronous Writing =======================================")
const fs2 = require('fs');

const content = 'This is some content to write to the file.';

fs2.writeFile('example.txt', content, err => {
    if (err) {
        console.error(err);
        return;
    }
    console.log('File written successfully');
});

console.log("============================ Synchronous Writing =======================================")
const fs3 = require('fs');

const content1 = 'This is some content to write to the file.';

try {
    fs3.writeFileSync('example.txt', content1);
    console.log('File written successfully');
} catch (err) {
    console.error(err);
}

console.log("============================ Asynchronous Appending to Files =======================================")
const fs4 = require('fs');

const content2 = 'This content will be appended to the file.\n';

fs4.appendFile('example.txt', content2, err => {
    if (err) {
        console.error(err);
        return;
    }
    console.log('Content appended successfully');
});


console.log("============================ Synchronous Appending to Files =======================================")
const fs5 = require('fs');

const content3 = 'This content will be appended to the file.\n';

try {
    fs5.appendFileSync('example.txt', content3);
    console.log('Content appended successfully');
} catch (err) {
    console.error(err);
}

console.log("============================ Asynchronous Deleting Files =======================================")
const fs6 = require('fs');

fs6.unlink('example.txt', err => {
    if (err) {
        console.error(err);
        return;
    }
    console.log('File deleted successfully');
});


console.log("============================ Synchronous Deleting files =======================================")
const fs7 = require('fs');

try {
    fs7.unlinkSync('example.txt');
    console.log('File deleted successfully');
} catch (err) {
    console.error(err);
}


console.log("============================ Asynchronous Renaming files =======================================")
const fs8 = require('fs');

fs8.rename('oldname.txt', 'newname.txt', err => {
    if (err) {
        console.error(err);
        return;
    }
    console.log('File renamed successfully');
});


console.log("============================ Synchronous Renaming files =======================================")
const fs9 = require('fs');

try {
    fs9.renameSync('oldname.txt', 'newname.txt');
    console.log('File renamed successfully');
} catch (err) {
    console.error(err);
}

console.log("============================ Combining multiple operations =======================================")
const fs = require('fs');

// Write to a new file
fs.writeFileSync('testfile.txt', 'Hello, world!\n');

// Read the file content
const data = fs.readFileSync('testfile.txt', 'utf8');
console.log('File content:', data);

// Append to the file
fs.appendFileSync('testfile.txt', 'Appending some text.\n');

// Read the updated file content
const updatedData = fs.readFileSync('testfile.txt', 'utf8');
console.log('Updated file content:', updatedData);

// Delete the file
fs.unlinkSync('testfile.txt');
console.log('File deleted successfully');

/*
Summary:
=======
1. fs.readFile / fs.readFileSync: Read files.
2. fs.writeFile / fs.writeFileSync: Write to files (overwrite if they exist).
3. fs.appendFile / fs.appendFileSync: Append to files.
4. fs.unlink / fs.unlinkSync: Delete files.
5. fs.rename / fs.renameSync: Rename files.

*/