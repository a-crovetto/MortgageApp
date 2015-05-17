
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
    console.log("form submitted!")  // sanity check
    console.log($('#' + this.id + '>td:nth-child(1)').text() )
    console.log($('#' + this.id + '>td:nth-child(2)').text() )
    console.log($('#principal').text() )
    console.log($('#interest').text() )
    console.log($('#' + this.id + '>td:nth-child(2)').text() )
    return false
});

function adjustmentSucces(data,textStatus,jqXHR)
{
    $('#adjustmentTable').html(data);
}