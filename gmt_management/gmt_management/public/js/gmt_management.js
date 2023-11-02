frappe.workspace.page.clear_primary_action();
frappe.workspace.page.clear_secondary_action();
frappe.workspace.page.clear_inner_toolbar();

$(document).on('DOMNodeInserted', "#body", function(e){
    $id = $(e.target).attr("id");
    if($id){
    if ($id.localeCompare('page-Workspaces') == 0) {
    if(frappe.user_roles.includes("Administrator")){
    $(function() {
    $("#page-Workspaces .page-actions").html("")
    })
    }
    }
    }
    });

