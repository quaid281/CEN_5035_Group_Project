const {Storage} = require('@google-cloud/storage');

const bucketName = process.env.BUCKET_NAME;
const keyFilename = 'app/config/service_account.json';
const projectId = process.env.PROJECT_ID;
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
  const file = await storage.bucket(bucketName).file(imagename);
  let image = {
    name: file.name,
    classification: file.name.substring(0, file.name.indexOf('-')),
    publicUrl: `https://storage.googleapis.com/${bucketName}/${file.name}`
  };
  res.status(200).send(image);
}

exports.updateImage = async (req, res) => {
  const image = req.body;
  const newClassification = image.classification + "-";
  const newName = newClassification + image.name.substring(image.name.indexOf('-')+1);
  const file = await storage.bucket(bucketName).file(image.name).rename(newName);
  image.name = newName;
  res.status(200).send(image);
}