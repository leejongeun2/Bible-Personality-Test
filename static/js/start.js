const main = document.querySelector("#main"); 
const qna = document.querySelector("#qna");
const result = document.querySelector('#result');
const endPoint = 12;
const select = [];


function calResult(){
    var pointArray = [
        { name: 'I', value: 0, key: 0}, //1
        { name: 'E', value: 0, key: 1}, //1 + 1 
        { name: 'S', value: 0, key: 2}, //1 + 1
        { name: 'N', value: 0, key: 3}, //1
        { name: 'T', value: 0, key: 4}, //1 + 1
        { name: 'F', value: 0, key: 5}, //1
        { name: 'P', value: 0, key: 6}, //1+1
        { name: 'J', value: 0, key: 7}, //1
        // { name: '누가', value: 0, key: 8}, 
        // { name: '마가', value: 0, key: 9}, 
        // { name: '룻', value: 0, key: 10},
        // { name: '아브라함', value: 0, key: 11},
        // { name: '드보라', value: 0, key: 12},
        // { name: '요한', value: 0, key: 13},
        // { name: '예레미야', value: 0, key: 14},
        // { name: '모세', value: 0, key: 15},
    ]

    for(let i = 0; i < endPoint; i++){ //문제 수
        var target = qnaList[i].a[select[i]]; //특정 문제의 답변에 선택한 답변 ex)1,0,1,0중 1번문제에 대한 답숫자
        for(let k = 0; k < pointArray.length; k++){
            if(target.type[0] === pointArray[k].name){
                pointArray[k].value += 1;
            }
        }
        }
    }



function goResult(){
    qna.style.display = "none";
    result.style.display = "block";
    console.log(select);

}

function addAnswer(answerText, qIdx, idx){
    var a = document.querySelector('.answerBox');
    var answer = document.createElement('button');
    answer.classList.add('answerList');
    a.appendChild(answer);
    answer.innerHTML = answerText;

    answer.addEventListener("click", function(){
        var children = document.querySelectorAll('.answerList')
        for(let i = 0; i < children.length; i++){
            children[i].disabled = true;
            select[qIdx] = idx;
            children[i].style.display = 'none';
        }
        goNext(++qIdx);
    }, false);
}

function goNext(qIdx){
    if(qIdx + 1 === endPoint){ 
        goResult();
        return;
    }

    var q = document.querySelector('.qBox');
    q.innerHTML = qnaList[qIdx].q;
    for(let i in qnaList[qIdx].a){
        addAnswer(qnaList[qIdx].a[i].answer, qIdx, i);
    }
    var progress = document.querySelector('.progress-bar');
    progress.style.width = (100/endPoint) * (qIdx+1) + '%';
}


function begin(){
    main.style.display = "none";
    qna.style.display = "block";
    let qIdx = 0;
    goNext(qIdx);
}

// let qIdx = 0;



