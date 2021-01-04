$(document).ready(function() {
    $('#sidebarCollapse').on('click', function() {
        $('#sidebar').toggleClass('active');
    });
    
    $('#userTable').DataTable({
        "columnDefs": [
            { "orderable": false, "targets": [4] },
            { "orderable": true, "targets": [0, 1, 2, 3] }
        ]
    });
});