$(document).ready(() => {
    $('#imageInput').on('change', (e) => {
        try {
            var reader = new FileReader()

            reader.onload = (e) => {
                $('#imagePreview').attr('src', e.target.result)
            }

            reader.readAsDataURL(e.target.files[0])
        } catch (err) {
            console.log(err)
        }
    })
})