// cnpj_mask.js
$(document).ready(function() {
    $('#id_cnpj').on('input', function() {
        var cnpj = $(this).val().replace(/\D/g, '');
        if (cnpj.length > 2 && cnpj.length <= 5) {
            $(this).val(cnpj.substring(0, 2) + '.' + cnpj.substring(2));
        } else if (cnpj.length > 5 && cnpj.length <= 8) {
            $(this).val(cnpj.substring(0, 2) + '.' + cnpj.substring(2, 5) + '.' + cnpj.substring(5));
        } else if (cnpj.length > 8 && cnpj.length <= 12) {
            $(this).val(cnpj.substring(0, 2) + '.' + cnpj.substring(2, 5) + '.' + cnpj.substring(5, 8) + '/' + cnpj.substring(8));
        } else if (cnpj.length > 12 && cnpj.length <= 14) {
            $(this).val(cnpj.substring(0, 2) + '.' + cnpj.substring(2, 5) + '.' + cnpj.substring(5, 8) + '/' + cnpj.substring(8, 12) + '-' + cnpj.substring(12));
        }
    });
});