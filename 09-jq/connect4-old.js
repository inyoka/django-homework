var player1 = prompt("Red player enter your name.")
var player1Color = 'rgb(255, 255, 51)';

var player2 = prompt("Yellow player enter your name.")
var player2Color = 'rgb(237, 45, 73)';

var player0Color = 'rgb(128, 128, 128)'

var game_on = true;
var table = $('table tr');

function reportWin(rowNum, colNum){
  console.log("You won starting at this col, row...");
  console.log(colNum, rowNum);
}

function changeColor(rowIndex, colIndex, color){
  return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color', color);
}

function returnColor(rowIndex, colIndex){
  return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
}

// Math.abs(row - 6)

function checkBottom(colIndex){
  var colorReport = returnColor(5, colIndex);
  for (var row = 5; row > -1; row--) {
    colorReport = returnColor(row,colIndex);
    console.log('trying loop');
    // console.log(button.css('background-color'));
    if (colorReport === 'rgb(128, 128, 128)') {
      console.log('loop activated');
      return row
    }
  }
}

function colorMatchCheck(one, two, three, four){
  return (one === two && one === three && one === four && one!==undefined && one == (player1Color || player2Color))
}


// Check for Horizontal Wins
function horizontalWinCheck() {
  for (var row = 0; row < 6; row++) {
    for (var col = 0; col < 4; col++) {
      if (colorMatchCheck(returnColor(row,col), returnColor(row,col+1) ,returnColor(row,col+2), returnColor(row,col+3))) {
        console.log('horiz');
        reportWin(row,col);
        return true;
      }else {
        continue;
      }
    }
  }
}

// Check for Vertical Wins
function verticalWinCheck() {
  for (var col = 0; col < 7; col++) {
    for (var row = 0; row < 3; row++) {
      if (colorMatchCheck(returnColor(row,col), returnColor(row+1,col) ,returnColor(row+2,col), returnColor(row+3,col))) {
        console.log('vertical');
        reportWin(row,col);
        return true;
      }else {
        continue;
      }
    }
  }
}

// Check for Diagonal Wins
function diagonalWinCheck() {
  for (var col = 0; col < 5; col++) {
    for (var row = 0; row < 7; row++) {
      if (colorMatchCheck(returnColor(row,col), returnColor(row+1,col+1) ,returnColor(row+2,col+2), returnColor(row+3,col+3))) {
        console.log('diag');
        reportWin(row,col);
        return true;
      }else if (colorMatchCheck(returnColor(row,col), returnColor(row-1,col+1) ,returnColor(row-2,col+2), returnColor(row-3,col+3))) {
        console.log('diag');
        reportWin(row,col);
        return true;
      }else {
        continue;
      }
    }
  }
}
function gameEnd(winningPlayer) {
  for (var col = 0; col < 7; col++) {
    for (var row = 0; row < 7; row++) {
      $('h3').fadeOut('fast');
      $('h2').fadeOut('fast');
      $('h1').text(winningPlayer+" has won! Refresh your browser to play again!").css("fontSize", "50px")
    }
  }
}

var currentPlayer = 1;
var currentName = player1;
var currentColor = player1Color;

$('h3').text(player1+" it's your turn.");
$('.board button').on('click', function(){


  var col = $(this).closest('td').index();
  var bottomAvail = checkBottom(col);
  changeColor(bottomAvail,col,currentColor);

  if (horizontalWinCheck() || verticalWinCheck() || diagonalWinCheck()) {
    gameEnd(currentName);
  }
  currentPlayer = currentPlayer * -1;

  if (currentPlayer === 1) {
    currentName = player1;
    $('h3').text(currentName+" it is your turn.");
    currentColor = player1Color;
    $('h3').css('background-color', player1Color)
  } else {
    currentName = player2;
    $('h3').text(currentName+" it is your turn.");
    currentColor = player2Color;
        $('h3').css('background-color', player2Color)
  }
})
