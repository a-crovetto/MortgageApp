
$('[name="calc-rows"]').on('click', function(){
    $.ajax({
       type:"GET",
       url:"test/",
       data: {       
        'years' : $('#' + this.id + '>td:nth-child(1)').text(),
        'monthly' : $('#' + this.id + '>td:nth-child(2)').text(),
        'principal' : $('#principal').text(),
        'interest' : $('#interest').text()
       },
       success: adjustmentSucces
    })
    $(this).addClass( "highlight-row" ).siblings().removeClass('highlight-row');
});

function adjustmentSucces(data,textStatus,jqXHR)
{
    $('#adjustmentTable').html(data);
}