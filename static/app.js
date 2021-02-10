

// $('#guessBtn').on('click', function(e){
//     e.preventDefault();
//     let word = $('#guessInp').val()
//     result = getData(word)
//     console.log(`Value of result in first func ${result}`)
//     e.setTimeOut(msg(result),3000)
// }
// )

async function getData(str){
    const response = await axios.get('http://127.0.0.1:5000/checkWord', { params: { str } })
    const result = response.data.result;
    console.log(`this is from inside getdata ${result}`);
    console.log(response)
    return result
    }

function msg(str){
    $('.messages').css('display','block')
    p = $('p')
    console.log(`value of result in msg funct = ${str}`)
    if (str == 'ok') {
        p.addClass('success')
        p.html('Valid word!!')}
    else {
        p.addClass('error')
        p.html('Invalid word!!')}
    console.log('run the msg function')
    return 
}
let word = $('#guessInp').val()
// console.log(`this is get data ${getData('adsd')}`)
getData(word).then(res=>
    {

$('#guessBtn').on('click', function(e){
    e.preventDefault();
    // let word = $('#guessInp').val()
    result = res
    console.log(`Value of result in first func ${result}`)
    e.setTimeOut(msg(result),3000)
}
)
    }
    )
