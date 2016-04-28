var textFile = null;
var output = '';
var corpus = null;

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

function checkFragment(caseNumber, first, last) {
  if (corpus != null) {
    var words = {};
    for (var i = (first-1); i < last; i++) {
      var wordToCheck = corpus[i];
      if (!(wordToCheck in words)) {
        words[wordToCheck] = 1;
      } else {
        words[wordToCheck] += 1;
      }
    }

    var orderedWords = [{
      'word': '',
      'frequency': 0
    }, {
      'word': '',
      'frequency': 0
    }, {
      'word': '',
      'frequency': 0
    }];

    for (var word in words) {

      var wordDict = {
        'word': word,
        'frequency': words[word]
      };

      for (var i=0; i<3; i++) {
        if (orderedWords[i].frequency < words[word]) {
          orderedWords.splice(i, 0, wordDict);
          break;
        }
      }
    }

    var text = 'Case #' + caseNumber + ': ' + orderedWords[0].word + ' ' + orderedWords[0].frequency + ','  + orderedWords[1].word + ' ' + orderedWords[1].frequency + ','  + orderedWords[2].word + ' ' + orderedWords[2].frequency ;
    output += (text + '\n');
    $('.js-result').append(text + '<br>');
  }
}

$('.js-corpus').change(function(){
  var file = this.files[0];
  var reader = new FileReader();
  reader.onload = function(progressEvent){
    var lines = this.result.split('\n');
    corpus = lines[0].split(' ');
  };
  reader.readAsText(file);
});

$('.js-input').change(function(){

  var file = this.files[0];

  var reader = new FileReader();
  reader.onload = function(progressEvent){
    var lines = this.result.split('\n');

    var fragments = parseInt(lines[0]);
    for(var line = 1; line <= fragments; line++){
      var indexes = lines[line].split(' ');
      var first = parseInt(indexes[0]);
      var last = parseInt(indexes[1]);
      checkFragment(line, first, last)
    }

    $('.js-download').attr('href', makeTextFile(output))
  };
  reader.readAsText(file);
});

