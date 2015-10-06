module.exports = function (grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        copy: {
            fonts: {
                files: [
                    {
                        expand: true,
                        src: [
                            'bower_components/components-font-awesome/fonts/*'
                        ],
                        dest: 'static/fonts/',
                        flatten: true,
                    },
                    {
                        expand: true,
                        src: [
                            'bower_components/components-font-awesome/css/*'
                        ],
                        dest: 'static/css',
                        flatten: true,
                    },
                ]
            }
        },

        sass: {
            dist: {
                options: {
                    loadPath: 'bower_components/foundation/scss',
                },
                files: [{
                    expand: true,
                    src: ['scss/*.scss'],
                    dest: 'static/css/',
                    flatten: true,
                    ext: '.css',
                }],
            }
        },

        concat: {
            options: {
                separator: ';\n',
            },
            scripts: {
                src: ['<%= pkg.jsFiles %>'],
                dest: 'static/js/scripts.js',
            },
        },

        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> <%= grunt.template.today("dd-mm-yyyy") %> */\n',
            },
            scripts: {
                files: {
                    'static/js/scripts.min.js': ['<%= concat.scripts.dest %>'],
                },
            },
        },

        watch: {
            sass: {
                files: ['scss/**/*.scss'],
                tasks: ['sass'],
                options: {
                    interrupt: true,
                },
            },
            js: {
                files: ['js/**/*.js', 'package.json'],
                tasks: ['js'],
                options: {
                    interrupt: true,
                },
            },
        },
    });

    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('js', ['concat', 'uglify']);
    grunt.registerTask('default', ['copy', 'sass', 'js']);
};
