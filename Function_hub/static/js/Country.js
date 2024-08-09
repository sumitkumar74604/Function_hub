// document.addEventListener('DOMContentLoaded', function() {
//     console.log('DOM fully loaded and parsed');

//     // Select elements
//     const billingCountrySelect = document.getElementById('billing-country');
//     const billingStateSelect = document.getElementById('billing-state');
//     const shippingCountrySelect = document.getElementById('shipping-country');
//     const shippingStateSelect = document.getElementById('shipping-state');
//     const registrationCountrySelect = document.getElementById('Registration-country');
//     const registrationStateSelect = document.getElementById('Registration-state');

//     // Function to fetch countries and populate dropdowns
//     function populateCountries() {
//         fetch('/api/countries/')
//             .then(response => {
//                 console.log('Fetching countries:', response);
//                 return response.json();
//             })
//             .then(data => {
//                 console.log('Countries data:', data);
//                 const countryOptions = data.map(country => {
//                     const option = document.createElement('option');
//                     option.value = country.code;
//                     option.textContent = country.name;
//                     return option;
//                 });

//                 // Clear existing options and populate country dropdowns
//                 [billingCountrySelect, shippingCountrySelect, registrationCountrySelect].forEach(select => {
//                     select.innerHTML = '<option selected disabled>Country</option>';
//                     countryOptions.forEach(option => select.appendChild(option.cloneNode(true)));
//                 });
//             })
//             .catch(error => console.error('Error fetching countries:', error));
//     }

//     // Function to fetch states based on country code
//     function populateStates(select, countryCode) {
//         fetch(`/api/states/${countryCode}/`)
//             .then(response => {
//                 console.log(`Fetching states for ${countryCode}:`, response);
//                 return response.json();
//             })
//             .then(data => {
//                 console.log('States data:', data);
//                 select.innerHTML = '<option selected disabled>States</option>'; // Reset state dropdown
//                 data.forEach(state => {
//                     const option = document.createElement('option');
//                     option.value = state.code;
//                     option.textContent = state.name;
//                     select.appendChild(option);
//                 });
//             })
//             .catch(error => console.error('Error fetching states:', error));
//     }

//     // Event listeners for country changes
//     if (billingCountrySelect) {
//         billingCountrySelect.addEventListener('change', function() {
//             populateStates(billingStateSelect, billingCountrySelect.value);
//         });
//     }

//     if (shippingCountrySelect) {
//         shippingCountrySelect.addEventListener('change', function() {
//             populateStates(shippingStateSelect, shippingCountrySelect.value);
//         });
//     }

//     if (registrationCountrySelect) {
//         registrationCountrySelect.addEventListener('change', function() {
//             populateStates(registrationStateSelect, registrationCountrySelect.value);
//         });
//     }

//     // Initial population of country dropdowns
//     populateCountries();
// });

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded and parsed');

    // Select elements
    const billingCountrySelect = document.getElementById('billing-country');
    const billingStateSelect = document.getElementById('billing-state');
    const shippingCountrySelect = document.getElementById('shipping-country');
    const shippingStateSelect = document.getElementById('shipping-state');
    const registrationCountrySelect = document.getElementById('Registration-country');
    const registrationStateSelect = document.getElementById('Registration-state');

    // Function to fetch countries and populate dropdowns
    function populateCountries() {
        console.log('Fetching countries...');
        fetch('/api/countries/')
            .then(response => {
                console.log('Response status:', response.status);
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log('Countries data:', data);
                const countryOptions = data.map(country => {
                    const option = document.createElement('option');
                    option.value = country.code;
                    option.textContent = country.name;
                    return option;
                });

                // Clear existing options and populate country dropdowns
                [billingCountrySelect, shippingCountrySelect, registrationCountrySelect].forEach(select => {
                    if (select) {
                        select.innerHTML = '<option selected disabled>Country</option>';
                        countryOptions.forEach(option => select.appendChild(option.cloneNode(true)));
                    }
                });
            })
            .catch(error => console.error('Error fetching countries:', error));
    }

    // Function to fetch states based on country code
    function populateStates(select, countryCode) {
        if (!select) return;
        console.log(`Fetching states for ${countryCode}...`);
        fetch(`/api/states/${countryCode}/`)
            .then(response => {
                console.log('Response status:', response.status);
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log('States data:', data);
                select.innerHTML = '<option selected disabled>States</option>'; // Reset state dropdown
                data.forEach(state => {
                    const option = document.createElement('option');
                    option.value = state.code;
                    option.textContent = state.name;
                    select.appendChild(option);
                });
            })
            .catch(error => console.error('Error fetching states:', error));
    }

    // Event listeners for country changes
    if (billingCountrySelect) {
        billingCountrySelect.addEventListener('change', function() {
            console.log('Billing country changed to:', billingCountrySelect.value);
            populateStates(billingStateSelect, billingCountrySelect.value);
        });
    }

    if (shippingCountrySelect) {
        shippingCountrySelect.addEventListener('change', function() {
            console.log('Shipping country changed to:', shippingCountrySelect.value);
            populateStates(shippingStateSelect, shippingCountrySelect.value);
        });
    }

    if (registrationCountrySelect) {
        registrationCountrySelect.addEventListener('change', function() {
            console.log('Registration country changed to:', registrationCountrySelect.value);
            populateStates(registrationStateSelect, registrationCountrySelect.value);
        });
    }

    // Initial population of country dropdowns
    populateCountries();
});
