const $ = window.$;
$(document).ready(function () {
  $('HEADER').on({
    click: function () {
      if ($('HEADER').hasClass('red')) {
        $('HEADER').removeClass('red');
        $('HEADER').addClass('green');
      } else {
        $('HEADER').removeClass('green');
        $('HEADER').addClass('red');
      }
    }
  });
});
