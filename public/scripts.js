$(document).ready(() => {
    $('#imageInput').on('change', (e) => {
        try {
            let reader = new FileReader()

            reader.onload = (e) => {
                $('#imagePreview').attr('src', e.target.result)
            }

            reader.readAsDataURL(e.target.files[0])
        } catch (err) {
            console.log(err)
        }
    })

    $('#ccButton').on('click', () => {
        try {
            if ($('#imagePreview').attr('src') != null) {
                $('<a>', {
                    href: $('#imagePreview').attr('src'), download: 'color-correct-image.jpg',
                }).appendTo('body').get(0).click().remove()
            }
        } catch (err) {
        }
    })

    $('#edButton').on('click', () => {
        try {
            if ($('#imagePreview').attr('src') != null) {
                $('<a>', {
                    href: $('#imagePreview').attr('src'), download: 'edge-detected-image.jpg',
                }).appendTo('body').get(0).click().remove()
            }
        } catch (err) {
        }
    })
})