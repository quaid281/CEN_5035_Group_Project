const express = require('express');
const {Storage} = require('@google-cloud/storage');

const app = express();
const port = process.env.PORT || 8080;

const bucketName = process.env.BUCKET_NAME;
const keyFilename = process.env.KEYFILE;
const projectId = process.env.PROJECT_ID;
const storage = new Storage({projectId, keyFilename});

app.use('/', express.static('dist/angular-client'));
app.get('/cloudimages', async (req,res) => {
    const [files] = await storage.bucket(bucketName).getFiles();
    let images = [];
    files.forEach(async file => {
        image = {
            name: file.name,
            publicUrl: `https://storage.googleapis.com/${bucketName}/${file.name}`
        }
        images.push(image);
      });
    res.status(200).send(images);
})

app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});