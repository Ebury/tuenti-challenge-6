var textFile = null;
var output = '';

function makeTextFile(text) {
  var data = new Blob([text], {type: 'text/plain'});

  // If we are replacing a previously generated file we need to
  // manually revoke the object URL to avoid memory leaks.
  if (textFile !== null) {
    window.URL.revokeObjectURL(textFile);
  }

  textFile = window.URL.createObjectURL(data);

  // returns a URL you can use as a href
  return textFile;
}

function teamLunch(caseNumber, diners) {
  if (!isNaN(diners)) {
    var notSeated = diners;
    var tables = 0;
    while (notSeated !== 0) {
      tables++;
      if (tables === 1) {
        notSeated -= 3;
      } else {
        notSeated -= 2;
      }
      if (notSeated === 1 || notSeated < 0) {
        notSeated = 0;
      }
    }
    var text = 'Case #' + caseNumber + ': ' + tables;
    output += (text + '\n');
    $('.js-result').append(text + '<br>');
  }
}

$('.js-file').change(function(){

  var file = this.files[0];

  var reader = new FileReader();
  reader.onload = function(progressEvent){

    // By lines
    var lines = this.result.split('\n');

    var cases = parseInt(lines[0]);
    for(var line = 1; line <= cases; line++){
      teamLunch(line, parseInt(lines[line]))
    }

    $('.js-download').attr('href', makeTextFile(output))
  };
  reader.readAsText(file);
});

