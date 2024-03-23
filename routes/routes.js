const express = require('express')
const controller = require('../controllers/controller.js')
const app = express()

app.get('/favicon.ico', controller.showIcon)
app.get('/', controller.showIndex)

module.exports = app