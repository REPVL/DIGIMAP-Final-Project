$(document).ready(() => {
    $('#imageInput').on('change', (e) => {
        try {
            let reader = new FileReader()

            reader.onload = (e) => {
                $('#imagePreview').attr('src', e.target.result);
                $('#ccPreview').attr('src', e.target.result);
                $('#edPreview').attr('src', e.target.result);
            }

            reader.readAsDataURL(e.target.files[0])
        } catch (err) {
            console.log(err)
        }
    })

    $('#ccButton').on('click', () => {
        try {
            if ($('#ccPreview').attr('src') !== '') {
                let colorCorrectedDataURL = $('#ccPreview').attr('src');
                $('<a>', {
                    href: colorCorrectedDataURL,
                    download: 'color-corrected-image.jpg',
                }).appendTo('body').get(0).click().remove()
            }
        } catch (err) {
            console.log('Error occured.');
        }
    })

    $('#edButton').on('click', () => {
        try {
            if ($('#edPreview').attr('src') !== '') {
                let edgeDetectedDataURL = $('#edPreview').attr('src');
                $('<a>', {
                    href: edgeDetectedDataURL,
                    download: 'edge-detected-image.jpg',
                }).appendTo('body').get(0).click().remove()
            }
        } catch (err) {
            console.log('Error Occured.');
        }
    })
})