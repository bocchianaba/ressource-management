let list = document.querySelectorAll(".navigation li");

function activeLink(){
    list.forEach(item=>{
        item.classList.remove("hovered");
    })
    this.classList.add("hovered");
}

list.forEach(item=>item.addEventListener("mouseover", activeLink))

//menu toggle
let toggle = document.querySelector(".toggle");
let navigation = document.querySelector(".navigation");
let main = document.querySelector(".main");

toggle.onclick = function(){
    navigation.classList.toggle("active");
     main.classList.toggle("active");
};

let contractCount = 0;

function showForm() {
  document.getElementById('formPopup').style.display = 'block';
  document.querySelector('.overlay').style.display = 'block';
}

function closeForm() {
  document.getElementById('formPopup').style.display = 'none';
  document.querySelector('.overlay').style.display = 'none';
}

function generateContract() {
  const contractName = document.getElementById('contractName').value;
  const clientName = document.getElementById('clientName').value;
  const providerName = document.getElementById('providerName').value;
  const projectDescription = document.getElementById('projectDescription').value;
  const projectBudget = document.getElementById('projectBudget').value;
  const contractDuration = document.getElementById('contractDuration').value;
  const maxChanges = document.getElementById('maxChanges').value;

  if (contractName && clientName && providerName && projectBudget && contractDuration && maxChanges) {
    contractCount++;
    const table = document.getElementById('contractTable');
    const row = table.insertRow();
    const cell1 = row.insertCell(0);
    const cell2 = row.insertCell(1);
    cell1.textContent = contractCount;
    cell2.textContent = contractName;
    cell2.onclick = function() { showContract(contractName, clientName, providerName, projectDescription, projectBudget, contractDuration, maxChanges); };
    closeForm();
  }
}

function showContract(contractName, clientName, providerName, projectDescription, projectBudget, contractDuration, maxChanges) {
  const popup = document.getElementById('contractPopup');
  popup.innerHTML = '<h3>' + contractName + '</h3><p><strong>Client:</strong> ' + clientName + '</p><p><strong>Prestataire:</strong> ' + providerName + '</p><p><strong>Description du Projet:</strong> ' + projectDescription + '</p><p><strong>Budget du Projet:</strong> ' + projectBudget + '</p><p><strong>Durée du Contrat:</strong> ' + contractDuration + '</p><p><strong>Nombre Max de Modifications:</strong> ' + maxChanges + '</p><button style="background-color: #4CAF50; border:none; color: white; padding: 10px 20px; margin-right: 10px; text-align-center; display: inline-block; text-decoration: none; font-size: 12px; cursor: pointer; border-radius: 4px;"  class="button" onclick="printContract()"> <ion-icon name="print"></ion-icon> Imprimer</button>';
  popup.style.display = 'block';
  document.querySelector('.overlay').style.display = 'block';
}

function closePopup() {
    document.getElementById('formPopup').style.display = 'none';
  document.getElementById('contractPopup').style.display = 'none';
  document.querySelector('.overlay').style.display = 'none';
}

function printContract() {
  const popupContent = document.getElementById('contractPopup').innerHTML;
  const originalContent = document.body.innerHTML;
  document.body.innerHTML = popupContent;
  window.print();
  document.body.innerHTML = originalContent;
}