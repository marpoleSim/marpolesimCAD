function selectParts(data) {
   //var html = '<div> jjj';
   //html += '    <form name="selectPartForm" id="selectPartForm">';
   //html += '    {% csrf_token %}';
   //html += '    <select class="form-select" name="partList" id="partList" required autocomplete="off">';
   //html += '     <option disabled selected value>Select a part...</option>';
   //html += '   {% for value in data %}';
   //html += '     <option value="{{value}}">{{value}}</option>';
   //html += '     {% endfor %}';
   //html += '    </select>';
   //html += '    </div> '; 
   //html += '    <input style="margin: 20px;" type="submit" value="Select">';
   //html += '    </form>';
   //html += '    </div>';
   //console.log(html);
   //document.getElementById('selectPartsA').innerHTML = html;
}

$(function () {

   $("#selectCompanyForm").on('submit', function (event) {
      event.preventDefault();

      $.ajax({
         url: 'select_part',
         type: 'POST',
         data: $(this).serialize(),
         dataType: 'json',
      //   success: function (response) {
      //      //selectParts(response);
      //   }
      });
   });

});
