function predit_weight(){
    let Vertical_input = document.getElementById('input_text_Vertical').value
    let Diagonal_input = document.getElementById('input_text_Diagonal').value
    let Cross_input = document.getElementById('input_text_Cross').value
    let Height_input = document.getElementById('input_text_Height').value
    let Width_input = document.getElementById('input_text_Width').value
    fish_weight=get_fish_prediction(Vertical_input,Diagonal_input,Cross_input,Height_input,Width_input)
}

function get_fish_prediction(Vertical_input,Diagonal_input,Cross_input,Height_input,Width_input){
    let fish_weight=0
    $.ajax({
        url: '/get_end_predictions',
        type: "post",
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify({
            "Vertical_input":Vertical_input,
            "Diagonal_input":Diagonal_input,
            "Cross_input":Cross_input,
            "Height_input":Height_input,
            "Width_input":Width_input
        })
    }).done(function (jsondata, textStatus, jqXHR) {
        fish_weight=jsondata
        console.log("get result:"+fish_weight)
        res_text=document.getElementById('result_output')
        res_text.value=fish_weight
    }).fail(function (jsondata, textStatus, jqXHR) {
        console.log("Fail:"+fish_weight)
        console.log(jsondata)
    })
    return fish_weight
}