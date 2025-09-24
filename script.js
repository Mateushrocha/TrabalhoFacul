const API_URL = "http://127.0.0.1:5000/imoveis";

        const form = document.getElementById('imovel-form');
        const imoveisList = document.getElementById('imoveis-list');
        const loadingMessage = document.getElementById('loading-message');
        
        const modal = document.getElementById('message-modal');
        const modalTitle = document.getElementById('modal-title');
        const modalMessage = document.getElementById('modal-message');
        const modalCloseBtn = document.getElementById('modal-close');

        let isEditing = false;
        let imovelIdToEdit = null;

        // Função para exibir o modal de mensagem
        function showMessageModal(title, message) {
            modalTitle.textContent = title;
            modalMessage.textContent = message;
            modal.classList.remove('hidden');
            modal.classList.add('flex');
        }

        // Função para fechar o modal
        modalCloseBtn.addEventListener('click', () => {
            modal.classList.remove('flex');
            modal.classList.add('hidden');
        });

        // Função para buscar e exibir os imóveis
        async function fetchImoveis() {
            loadingMessage.classList.remove('hidden');
            imoveisList.innerHTML = '';
            try {
                const response = await fetch(API_URL);
                if (!response.ok) throw new Error('Erro ao buscar os dados.');
                const imoveis = await response.json();
                
                if (imoveis.length === 0) {
                    imoveisList.innerHTML = '<p class="text-center text-gray-500">Nenhum imóvel cadastrado ainda.</p>';
                } else {
                    imoveis.forEach(imovel => {
                        const imovelCard = document.createElement('div');
                        imovelCard.className = 'bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex justify-between items-center';
                        imovelCard.innerHTML = `
                            <div>
                                <p class="font-bold text-gray-800">Endereço: ${imovel.endereco}</p>
                                <p class="text-sm text-gray-600">Proprietário: ${imovel.proprietario}</p>
                                <p class="text-sm text-gray-600">Entrada: ${imovel.entrada}</p>
                                <p class="text-sm text-gray-600">Valor: ${imovel.valor}</p>
                                <p class="text-sm text-gray-600">Descrição: ${imovel.descricao}</p>
                                <p class="text-xs text-gray-400 mt-2">ID: ${imovel.id}</p>
                            </div>
                            <div class="flex space-x-2">
                                <button onclick="prepararEdicao(${imovel.id})" class="bg-yellow-500 text-white px-3 py-1 rounded-md text-sm hover:bg-yellow-600 transition duration-300">Editar</button>
                                <button onclick="removerImovel(${imovel.id})" class="bg-red-500 text-white px-3 py-1 rounded-md text-sm hover:bg-red-600 transition duration-300">Remover</button>
                            </div>
                        `;
                        imoveisList.appendChild(imovelCard);
                    });
                }
            } catch (error) {
                console.error("Erro:", error);
                showMessageModal("Erro de Conexão", "Não foi possível conectar ao servidor Python. Por favor, certifique-se de que ele está rodando.");
            } finally {
                loadingMessage.classList.add('hidden');
            }
        }

        // Lógica para enviar o formulário
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const formData = {
                endereco: document.getElementById('endereco').value,
                proprietario: document.getElementById('proprietario').value,
                entrada: document.getElementById('entrada').value,
                valor: document.getElementById('valor').value,
                descricao: document.getElementById('descricao').value,
            };

            try {
                if (isEditing) {
                    await fetch(`${API_URL}/${imovelIdToEdit}`, {
                        method: 'PUT',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(formData)
                    });
                    isEditing = false;
                    imovelIdToEdit = null;
                    document.querySelector('#imovel-form button').textContent = 'Salvar Imóvel';
                    showMessageModal("Sucesso", "Imóvel atualizado com sucesso!");
                } else {
                    await fetch(API_URL, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(formData)
                    });
                    showMessageModal("Sucesso", "Imóvel adicionado com sucesso!");
                }
                
                form.reset();
                fetchImoveis();
            } catch (error) {
                console.error("Erro:", error);
                showMessageModal("Erro", "Não foi possível salvar os dados. Verifique a conexão.");
            }
        });

        // Função para preencher o formulário para edição
        async function prepararEdicao(id) {
            try {
                const response = await fetch(API_URL);
                const imoveis = await response.json();
                const imovel = imoveis.find(i => i.id === id);
                if (imovel) {
                    document.getElementById('endereco').value = imovel.endereco;
                    document.getElementById('proprietario').value = imovel.proprietario;
                    document.getElementById('entrada').value = imovel.entrada;
                    document.getElementById('valor').value = imovel.valor;
                    document.getElementById('descricao').value = imovel.descricao;
                    
                    isEditing = true;
                    imovelIdToEdit = id;
                    document.querySelector('#imovel-form button').textContent = 'Atualizar Imóvel';
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                }
            } catch (error) {
                console.error("Erro:", error);
            }
        }

        // Função para remover um imóvel
        async function removerImovel(id) {
            if (!confirm('Tem certeza que deseja remover este imóvel?')) {
                return; // Substituído por uma lógica simples, mas em uma aplicação real usaria um modal.
            }

            try {
                await fetch(`${API_URL}/${id}`, {
                    method: 'DELETE'
                });
                showMessageModal("Sucesso", "Imóvel removido com sucesso!");
                fetchImoveis();
            } catch (error) {
                console.error("Erro:", error);
                showMessageModal("Erro", "Não foi possível remover o imóvel. Verifique a conexão.");
            }
        }

        // Carrega os imóveis ao carregar a página
        window.onload = fetchImoveis;