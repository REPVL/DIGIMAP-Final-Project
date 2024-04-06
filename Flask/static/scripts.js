$(document).ready(function () {
    $('#file_input').on('change', function (event) {
        let reader = new FileReader()

        reader.onload = (event) => {
            $('#image_preview').attr('src', event.target.result);
        }

        reader.readAsDataURL(event.target.files[0])
    })

    $('.slider').each(function () {
        $(this).on('input', function () {
            $(this).next('.slider-value').text(parseInt(this.value * 100, 10))
        })
    })

    $('.processed-button').on('click', function () {
        let image_source = $(this).prev('.processed-image').attr('src');
        let $a = $('<a>')
            .attr('href', image_source)
            .attr('download', 'download.png')
            .appendTo('body');

        $a[0].click();
        $a.remove();
    });
})