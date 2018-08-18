$(document).ready(function() {
    $(".edititem").click(function() {
        todo_text = $(this).parent().children().first().text()
        $(this).next().css('display', 'block')
        edit_form = $(this).next().children().first()
        edit_input_field = $(edit_form).children().first().next().children().first() 
        $(edit_input_field).val(todo_text)
    })
});