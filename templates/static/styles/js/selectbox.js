  // Sample organization and volunteer data
  const organizations = [
    { id: 'org1', name: 'Organization 1' },
    { id: 'org2', name: 'Organization 2' },
    // Add more organizations as needed
  ];

  const volunteers = [
    { id: 'vol1', name: 'Volunteer 1' },
    { id: 'vol2', name: 'Volunteer 2' },
    // Add more volunteers as needed
  ];

  // Function to populate the dropdowns with options
  function populateDropdown(selectElement, data) {
    data.forEach(item => {
      const option = document.createElement('option');
      option.value = item.id;
      option.text = item.name;
      selectElement.appendChild(option);
    });
  }

  // Get the select elements
  const organizationSelect = document.getElementById('organizationId');
  const volunteerSelect = document.getElementById('volunteerId');

  // Populate the dropdowns with options
  populateDropdown(organizationSelect, organizations);
  populateDropdown(volunteerSelect, volunteers);
