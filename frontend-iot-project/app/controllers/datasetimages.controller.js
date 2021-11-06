const {Storage} = require('@google-cloud/storage');

const keyFilename = 'app/config/service_account.json';
const projectId = process.env.PROJECT_ID;
const bucketName = process.env.BUCKET_NAME || `iot-project_${projectId}`;
const storage = new Storage({projectId, keyFilename});

exports.findAll = async (req, res) => {
      const [files] = await storage.bucket(bucketName).getFiles();
      console.log('Retrieving images from cloud');
      let images = [];
      files.forEach(async file => {
          image = {
              name: file.name,
              classification: file.name.substring(0, file.name.indexOf('-')),
              publicUrl: `https://storage.googleapis.com/${bucketName}/${file.name}`
          }
          images.push(image);
        });
      res.status(200).send(images);
  }

exports.findImage = async (req, res) => {
  const imagename = req.params.image;
  try {
    const file = await storage.bucket(bucketName).file(imagename);
    const blobMetadata = await file.getMetadata();
    const metadata = blobMetadata[0].metadata;
    console.log('Metadata:' + metadata);
    let image = {
      name: file.name,
      classification: file.name.substring(0, file.name.indexOf('-')),
      publicUrl: `https://storage.googleapis.com/${bucketName}/${file.name}`,
      metadata: metadata
    };
    res.status(200).send(image);
  }
  catch {
    res.status(404).send({});
  }
  
}

exports.updateImage = async (req, res) => {
  const image = req.body;
  const newClassification = image.classification + "-";
  const newName = newClassification + image.name.substring(image.name.indexOf('-')+1);
  const file = await storage.bucket(bucketName).file(image.name).rename(newName);
  image.name = newName;
  res.status(200).send(image);
}