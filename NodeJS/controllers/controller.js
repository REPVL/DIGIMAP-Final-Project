const controller = {
    showIcon: (req, res) => {
        res.status(204).end()
    },

    showIndex: (req, res) => {
        res.send('index')
    }
}

module.exports = controller