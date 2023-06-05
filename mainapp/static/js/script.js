var vm = new Vue({
	el: '#app',
	data: {
		categories: [],
		works: [],
		selected_works: [],
		name_user: "",
		email_user: "",
		phone_user: ""
	},
	created: function () {
		axios.get('api/categories').then(function (response){
			vm.categories = response.data
		});
		axios.get('api/works').then(function (response){
			vm.works = response.data
		});
	},
	computed: {
		sum: function () {
			let str= JSON.stringify(this.selected_works, ['cost']).
				replace(/\[|\]|{|}|\"cost\":/g, '');
			let arr = str.split(',').filter((cost) => cost !== '');
			return arr.reduce(function(summa, elem) {
				return summa + Number(elem);
				}, 0);
		}
	},
	watch: {
		categories: function () {
			for(var i= 0; i < this.categories.length; i++) {
				this.selected_works[i] = [];
			}

		}
	},
	methods: {
		submit: function (){
			let str= JSON.stringify(this.selected_works, ['id']).
				replace(/\[|\]|{|}|\"id\":/g, '');
			let arr = str.split(',').filter((id) => id !== '');
			const user_and_user_choice = {
				user_name : this.name_user,
				user_email : this.email_user,
				user_phone : this.phone_user,
				user_choice : arr
			}
			alert(JSON.stringify(user_and_user_choice));
			str = JSON.stringify(user_and_user_choice)
			axios.post('http://localhost:8000/api/user_and_user_choice/', str)
			  .then((response) => {
				console.log(response);
			  })
			  .catch((error) => {
				console.log(error);
			  });
		}
	}
})
