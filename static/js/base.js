
// Add event listener on sidebar click after content is loaded
document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('sidebarCollapse').addEventListener('click', () => {
    $('#sidebar').toggleClass('hide');
    $('#principal').toggleClass('fullPage');
  })
})

// Replace data-feather for its icon
feather.replace()