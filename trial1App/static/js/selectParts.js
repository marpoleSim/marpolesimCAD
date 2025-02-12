function selectParts(data) {
   let select = document.getElementById("partList");
   select.innerHTML = "<option disabled selected value>Select a company...</option>";
   data.partList.forEach((partname, index) => { 
       let option = document.createElement("option");
       option.value = partname;
       option.text = partname;
       select.appendChild(option);
   });
}

$(function () {

   $("#selectCompanyForm").change(function (event) {
      event.preventDefault();

      $.ajax({
         url: 'select_part',
         type: 'POST',
         data: $(this).serialize(),
         dataType: 'json',
         success: function (response) {
            selectParts(response);
         }
      });
   });

});
