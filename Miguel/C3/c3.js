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

function outputTape(code, tapeNumber, content) {

  content = content.split('');

  var currentCharPos = 0;
  var currentState = 'start';
  var currentChar = null;
  var currentCode = null;

  while (currentState !== 'end') {

    if (currentCharPos >= content.length) {
      currentChar = ' ';
    } else {
      currentChar = content[currentCharPos];
    }

    currentCode = code[currentState][currentChar];

    if ('write' in currentCode) {
      content[currentCharPos] = currentCode.write;
    }

    if ('move' in currentCode) {
      if (currentCode.move === 'right') {
        currentCharPos++;
      } else if (currentCode.move === 'left') {
        currentCharPos--;
      }
    }

    if ('state' in currentCode) {
      currentState = currentCode.state;
    }
  }

  var text = 'Tape #' + tapeNumber + ': ' + content.join('');
  output += (text + '\n');
  $('.js-result').append(text + '<br>');

}


$('.js-input').change(function(){

  var file = this.files[0];

  var reader = new FileReader();
  reader.onload = function(progressEvent){

    var data = YAML.parse(this.result);

    for (var tape in data.tapes) {
      outputTape(data.code, tape, data.tapes[tape]);
    }

    $('.js-download').attr('href', makeTextFile(output))
  };
  reader.readAsText(file);
});

