$(document).ready(() => {
    $('#imageInput').on('change', (e) => {
        console.log('Hello');

        var reader = new FileReader()

        reader.onload = (e) => {
            $('#imagePreview').attr('src', e.target.result)
        }

        reader.readAsDataURL(e.target.files[0])
    })
})