#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

// Check if both the file path and content are provided as arguments
if (!filePath || !content) {
  console.error('Usage: ./1-writeme.js <file_path> <content>');
  process.exit(1);
}

// Write the content to the file in utf-8 encoding
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err); // Print the error object if an error occurs
  }
});

