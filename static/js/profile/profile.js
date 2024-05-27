// Проверка на пустые значения контактов
var isEmptyVK = document.getElementById('VK').innerHTML;
var isEmptyInstagram = document.getElementById('Instagram').innerHTML;
var isEmptyTelegram = document.getElementById('Telegram').innerHTML;
if (isEmptyVK == ""){
    document.getElementById('VK').style.display = 'none';
}
else{
    document.getElementById('VK').style.display = 'block';
}
if (isEmptyInstagram == ""){
    document.getElementById('Instagram').style.display = 'none';
}
else{
    document.getElementById('Instagram').style.display = 'block';
}
if (isEmptyTelegram == ""){
    document.getElementById('Telegram').style.display = 'none';
}
else{
    document.getElementById('Telegram').style.display = 'block';
}

function copyToClipboard(element) {
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val($(element).text()).select();
    document.execCommand("copy");
    // changeText()
    $temp.remove();
}

staticSrcBackImg = "'img/profile/backBtn.png'"
shortDescriptions = document.getElementsByClassName('shortDescription');
lengthS = shortDescriptions.length;
for (var i = 0; i < lengthS; i++) {
    shortDescription = shortDescriptions[i].textContent
    if (shortDescription.length > 100){
        document.getElementsByClassName('shortDescription')[i].textContent = shortDescription[0].toUpperCase() + shortDescription.slice(1,100) + '... ';
        document.getElementsByClassName('shortDescription')[i].innerHTML = document.getElementsByClassName('shortDescription')[i].innerHTML + "<a style='cursor: pointer; color: #9f67f8;' onclick='OpenShortDescription(this)' id='"+ i + "'>Читать далее</a>";
    }
    document.getElementsByClassName('backImgBox')[i].id = i
}

function OpenShortDescription(elt){
    cardBookElemOne = document.getElementsByClassName("cardBookElemOne")
    cardBookElemfullDescription = document.getElementsByClassName("cardBookElemfullDescription")
    length = cardBookElemOne.length;
    cardBookElemOne[elt.id].style.opacity = '0'
    cardBookElemOne[elt.id].style.zIndex = '0'
    cardBookElemfullDescription[elt.id].style.opacity = '1'
    cardBookElemfullDescription[elt.id].style.zIndex = '1'
}

function CloseShortDescription(elt){
    cardBookElemOne = document.getElementsByClassName("cardBookElemOne")
    cardBookElemfullDescription = document.getElementsByClassName("cardBookElemfullDescription")
    length = cardBookElemOne.length;
    cardBookElemOne[elt.id].style.opacity = '1'
    cardBookElemOne[elt.id].style.zIndex = '1'
    cardBookElemfullDescription[elt.id].style.opacity = '0'
    cardBookElemfullDescription[elt.id].style.zIndex = '0'
}

function openUpdateProfileForm(){
    document.getElementById("updateProfile").style.display = 'block';
}

function closeUpdateProfileForm(){
    document.getElementById("updateProfile").style.display = 'none';
}