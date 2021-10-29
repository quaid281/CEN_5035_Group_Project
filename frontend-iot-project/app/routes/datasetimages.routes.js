module.exports = app => {
    const datasetimages = require("../controllers/datasetimages.controller.js");
  
    var router = require("express").Router();
  
    router.get("/", datasetimages.findAll);
    router.get("/:image", datasetimages.findImage);
    router.put("/", datasetimages.updateImage);

    app.use('/api/datasetimages', router);
  };
  