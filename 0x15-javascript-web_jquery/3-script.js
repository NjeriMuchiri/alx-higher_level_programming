const $ = window.$;
$(document).ready(function () {
  $('DIV#red_header').on({
    click: function () {
      $('HEADER').addClass('red');
    }
  });
});
