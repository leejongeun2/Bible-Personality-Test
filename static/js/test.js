$('#choice').click(function (){
    var id = $(this).attr('id')
    $.ajax({
        url: '/question/',
        type: "POST",
        dataType: "json",
        data: {'id': questionid,
        'question': question,
        'answer1': answer1,
        'answer2': answer2,
        },
        success: function(data){
            console.log(data);
        },
        error: function (request, status, error) {
            console.log('failed');
        }
    }); 
})