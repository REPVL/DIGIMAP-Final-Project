const express = require('express')
const controller = require('../controllers/controller.js')
const app = express()

app.get('/', controller.showIndex)

module.exports = app