var songTable = $('#songTable').dataTable({

    "aaSorting": [],
    ajax: {
        url: '/music/songs/songTable/',
        dataSrc: 'results',
    },
    createdRow: function(row, data, dataIndex) {
        $(row).attr("meetingId", data["id"]);
        //$(row).addClass("link-style");
        //$(row).on("click", function(){window.location.href = window.location.protocol + "//" + window.location.host + "/salesx/leadDrilldown/?lead_id=" + $(this).attr("leadid");});
        //$(row).on("click", function(){window.location.href = window.location.protocol + "//" + window.location.host + "/salesx/dsr/" + $(this).attr("meetingId");});
    },
    columns: [
        {data: "contactName", render: function(data, type, full, meta){return '<img  src="'+window.location.protocol + '//' + window.location.host + '/static/img/' + 'guitar.png' +'">'}},
        {data: "title", render: function(data, type, full, meta){return data}},
        {data: "artist", render: function(data, type, full, meta){return data}},
        {data: "genre",render: function(data, type, full, meta){return data}},
        {data: "duration", render: function(data, type, full, meta){return data}},
        {data: "year", render: function(data, type, full, meta){return data}},
        // {data: "contactName", render: function(data, type, full, meta){return '<a style="color:black;display:block" href="'+window.location.protocol + '//' + window.location.host + '/salesx/dsr/' + full.id +'">'+data+'</a>'}},
    ],
    "columnDefs": [
      //{ "orderable": false, "targets": 4 }
    ],
    "processing": true,
    "serverSide": true,
});

function populateDataTableAjax(){
    songTable.load();
}