marked.setOptions({
    highlight: function (code, lang) {
        var language = Prism.languages[lang];
        if (language) {
            return Prism.highlight(code, language, lang);
        }
        return code;
    }
});
var app = new Vue({
    el: '#app',
    data: {
        toc: [],
        keyword: '',
        cursor: '',
        list: [],
        key: '',
        markdown: '',
        mode: 'toc'
    },
    computed: {
        marked: function () {
            return this.markdown ? marked(this.markdown) : '';
        }
    },
    mounted: function () {
        this.getToc();
    },
    watch: {
        key: function (value) {
            if (value) {
                var self = this;
                axios.get(value).then(function (r) {
                    self.markdown = r.data;
                });
            }
        },
        keyword: function () {
            this.cursor = '';
        }
    },
    methods: {
        getToc: function() {
            var self = this;
            axios.get('.toc').then(function (r) {
                var toc = r.data.toc;
                var index = {'': {}};
                toc.forEach(function (key) {
                    var paths = key.split('/');
                    for (var i = 0; i < paths.length; i++) {
                        var childKey = paths.slice(0, i + 1).join('/');
                        if (index[childKey]) {
                            continue;
                        }
                        var childNode = {
                            id: (i === paths.length - 1) ? childKey : childKey + '/',
                            label: paths[i]
                        };
                        index[childKey] = childNode;

                        var parentKey = paths.slice(0, i).join('/');
                        var parentNode = index[parentKey];
                        if (parentNode.children == null) {
                            parentNode.children = [];
                        }
                        parentNode.children.push(childNode);
                    }
                });
                self.toc = index[''].children;
            });
        },
        onTocClick: function (data) {
            this.setKey(data.id);
        },
        onSearchClick: function(data) {
            this.setKey(data.key);
        },
        setKey: function(key) {
            if (!/\/$/.test(key)) {
                this.key = key;
            }
        },
        search: function () {
            var self = this;
            axios.get('.s', {
                params: {
                    q: self.keyword,
                    c: self.cursor,
                    n: 20
                }
            }).then(function (r) {
                self.list = r.data.list;
                self.cursor = r.data.cursor;
                self.mode = 'search';
            })
        }
    }
});