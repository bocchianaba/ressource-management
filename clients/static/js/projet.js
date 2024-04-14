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

let compteurProjet = 0;

document.getElementById('projetForm').addEventListener('submit', function(e) {
  e.preventDefault();
  ajouterProjet();
});

function afficherForm() {
  document.getElementById('formPopup').style.display = 'block';
  document.querySelector('.overlay').style.display = 'block';
}

function ajouterProjet() {
  const nom = document.getElementById('nom').value;
  const delai = document.getElementById('delai').value;
  const budget = document.getElementById('budget').value;
  const description = document.getElementById('description').value;
  /*const adresse = document.getElementById('adresse').value;*/

  // Regex pour valider le nom et le numéro de téléphone
  const regexNom = /^[A-Za-z0-9]+$/; // Lettres et chiffres uniquement
  /*const regexTelephone = /^[0-9+]+$/; // Chiffres et symbole de l'addition uniquement*/

  // Vérification des champs
  if (!regexNom.test(nom)) {
    alert('Le nom doit contenir uniquement des lettres et des chiffres.');
    return;
  }
  
  /*if (!regexTelephone.test(telephone) || telephone.length < 09) {
    alert('Le numéro de téléphone doit contenir uniquement des chiffres et le symbole +, et doit avoir au moins 09 caractères.');
    return;
  }

  if (!regexTelephone.test(telephone)) {
    alert('Le numéro de téléphone doit contenir uniquement des chiffres et le symbole +.');
    return;
  }*/
  if (nom && delai && budget && budget) {
    compteurProjet++;
    const table = document.getElementById('projetTable');
    const row = table.insertRow();
    const cell1 = row.insertCell(0);
    const cell2 = row.insertCell(1);
    cell1.textContent = compteurProjet;
    cell2.textContent = nom;
    cell2.onclick = function() { afficherPopup(nom, delai, budget, description); };
    fermerPopup();

    document.getElementById('nom').value = '';
    document.getElementById('delai').value = '';
    document.getElementById('budget').value = '';
    document.getElementById('description').value = '';
    /*document.getElementById('adresse').value = '';*/
  }
}

function afficherPopup(nom, delai, budget,description) {
  const popup = document.getElementById('popupInfo');
  popup.innerHTML = '<strong>Nom:</strong> ' + nom + '<br><strong>Delai de livraison:</strong> ' + delai+ '<br><strong>Budget alloué au projet:</strong> ' + budget+ '<br><strong>Description du projet:</strong> ' + description;
  popup.style.display = 'block';
  document.querySelector('.overlay').style.display = 'block';
}

function fermerPopup() {
  document.getElementById('formPopup').style.display = 'none';
  document.getElementById('popupInfo').style.display = 'none';
  document.querySelector('.overlay').style.display = 'none';
}
