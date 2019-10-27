$(document).ready(function(){
  // With JQuery
  $("#ex13").slider({
      ticks: [0, 100, 200, 300, 400],
      ticks_labels: ['$0', '$100', '$200', '$300', '$400'],
      ticks_snap_bounds: 30
  });

  // Without JQuery
  var slider = new Slider("#ex13", {
      ticks: [0, 100, 200, 300, 400],
      ticks_labels: ['$0', '$100', '$200', '$300', '$400'],
      ticks_snap_bounds: 30
  });

});
