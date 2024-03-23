const express = require('express')
const routes = require('./routes/routes.js')
const app = express()

app.use(express.json())
app.use(express.urlencoded({ extended: true }))
app.use(express.static('public'))
app.use('/', routes)

app.listen(8080, () => {
  console.log('Server is running at localhost:8080')
})