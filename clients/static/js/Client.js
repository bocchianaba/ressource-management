//add hovered class to selected list item
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

let compteurClient = 0;

document.getElementById('clientForm').addEventListener('submit', function(e) {
  if(!validerDonneeClient())
  e.preventDefault();
});

function afficherForm() {
  document.getElementById('formPopup').style.display = 'block';
  document.querySelector('.overlay').style.display = 'block';

  document.getElementById('nom').value = '';
  document.getElementById('telephone').value = '';
  document.getElementById('email').value = '';
  document.getElementById('adresse').value = '';
}

function validerDonneeClient() {
  const nom = document.getElementById('nom').value;
  const telephone = document.getElementById('telephone').value;
  const email = document.getElementById('email').value;
  const adresse = document.getElementById('adresse').value;

  console.log({nom, telephone, email, adresse})

  // Regex pour valider le nom et le numéro de téléphone
  const regexNom = /^[A-Za-z0-9]+$/; // Lettres et chiffres uniquement
  const regexTelephone = /^[0-9+]+$/; // Chiffres et symbole de l'addition uniquement

  // Vérification des champs
  // if (!regexNom.test(nom)) {
  //   alert('Le nom doit contenir uniquement des lettres et des chiffres.');
  //   return;
  // }
  
  if (!regexTelephone.test(telephone) || telephone.length < 9) {
    alert('Le numéro de téléphone doit contenir uniquement des chiffres et le symbole +, et doit avoir au moins 09 caractères.');
    return false;
  }

  if (!regexTelephone.test(telephone)) {
    alert('Le numéro de téléphone doit contenir uniquement des chiffres et le symbole +.');
    return false;
  }
  if (nom && telephone && email && adresse) {
    compteurClient++;
    // const table = document.getElementById('clientTable');
    // const row = table.insertRow();
    // const cell1 = row.insertCell(0);
    // const cell2 = row.insertCell(1);
    // cell1.textContent = compteurClient;
    // cell2.textContent = nom;
    // cell2.onclick = function() { afficherPopup(nom, telephone, email, adresse); };
    fermerPopup();
    return true
  }
  return true
}

function afficherPopup(nom, telephone, email, adresse) {
  const popup = document.getElementById('popupInfo');
  popup.innerHTML = '<strong>Nom:</strong> ' + nom + '<br><strong>Téléphone:</strong> ' + telephone + '<br><strong>Email:</strong> ' + email + '<br><strong>Adresse:</strong> ' + adresse;
  popup.style.display = 'block';
  document.querySelector('.overlay').style.display = 'block';
}

function fermerPopup() {
  document.getElementById('formPopup').style.display = 'none';
  document.getElementById('popupInfo').style.display = 'none';
  document.querySelector('.overlay').style.display = 'none';
}

function afficherPopupSuppression(id, name){
  if (confirm("Êtes-vous sûr de vouloir supprimer le client : "+name+" ?")) {
    // Si l'utilisateur confirme, envoyer une requête POST à la vue Django
    const deleteUrl = document.getElementById(`deleteBtn-${id}`).dataset.url;
    console.log({deleteUrl})
    window.location.href=deleteUrl
  }
}
